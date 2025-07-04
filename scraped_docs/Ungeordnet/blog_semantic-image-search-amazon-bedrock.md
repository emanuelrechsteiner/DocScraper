---
url: https://supabase.com/blog/semantic-image-search-amazon-bedrock
scraped_at: 2025-05-25T09:31:58.219280
title: Implementing semantic image search with Amazon Titan and Supabase Vector
---

  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
  * Product 
  * Developers 
  * [Enterprise](https://supabase.com/enterprise)
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[83.3K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# Implementing semantic image search with Amazon Titan and Supabase Vector
26 Mar 2024
•
9 minute read
[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)
![Implementing semantic image search with Amazon Titan and Supabase Vector](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fgetting-started%2Famazon-bedrock%2Famazon-bedrock-supabase-vecs.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Amazon Bedrock](https://aws.amazon.com/bedrock) is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon. Each model is accessible through a common API which implements a broad set of features to help build generative AI applications with security, privacy, and responsible AI in mind.
[Amazon Titan](https://aws.amazon.com/bedrock/titan/) is a family of foundation models (FMs) for text and image generation, summarization, classification, open-ended Q&A, information extraction, and text or image search.
In this post we'll look at how we can get started with Amazon Bedrock and Supabase Vector in Python using the Amazon Titan multimodal model and the [vecs client](https://supabase.com/docs/guides/ai/vecs-python-client).
You can find the full application code as a Python Poetry project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/aws_bedrock_image_search).
## Create a new Python project with Poetry[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#create-a-new-python-project-with-poetry)
[Poetry](https://python-poetry.org/) provides packaging and dependency management for Python. If you haven't already, install poetry via pip:
`
1
pip install poetry
`
Then initialize a new project:
`
1
poetry new aws_bedrock_image_search
`
## Spin up a Postgres Database with pgvector[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#spin-up-a-postgres-database-with-pgvector)
If you haven't already, head over to [database.new](https://database.new) and create a new project. Every Supabase project comes with a full Postgres database and the [pgvector extension](https://supabase.com/docs/guides/database/extensions/pgvector) preconfigured.
When creating your project, make sure to note down your database password as you will need it to construct the `DB_URL` in the next step.
You can find the database connection string in your Supabase Dashboard [project connect page](https://supabase.com/dashboard/project/_?showConnect=true). Select "Use connection pooling" with `Mode: Session` for a direct connection to your Postgres database. It will look something like this:
`
1
postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
`
## Install the dependencies[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#install-the-dependencies)
We will need to add the following dependencies to our project:
  * [`vecs`](https://github.com/supabase/vecs#vecs): Supabase Vector Python Client.
  * [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): AWS SDK for Python.
  * [`matplotlib`](https://matplotlib.org/): for displaying our image result.


`
1
poetry add vecs boto3 matplotlib
`
## Import the necessary dependencies[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#import-the-necessary-dependencies)
At the top of your main python script, import the dependencies and store your `DB URL` from above in a variable:
`
1
import sys
2
import boto3
3
import vecs
4
import json
5
import base64
6
from matplotlib import pyplot as plt
7
from matplotlib import image as mpimg
8
from typing import Optional
910
DB_CONNECTION = "postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres"
`
Next, get the [credentials to your AWS account](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) and instantiate the `boto3` client:
`
1
bedrock_client = boto3.client(
2
  'bedrock-runtime',
3
  region_name='us-west-2',
4
  # Credentials from your AWS account
5
  aws_access_key_id='<replace_your_own_credentials>',
6
  aws_secret_access_key='<replace_your_own_credentials>',
7
  aws_session_token='<replace_your_own_credentials>',
8
)
`
## Create embeddings for your images[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#create-embeddings-for-your-images)
In the root of your project, create a new folder called `images` and add some images. You can use the images from the example project on [GitHub](https://github.com/supabase/supabase/tree/master/examples/ai/aws_bedrock_image_search/images) or you can find license free images on [unsplash](https://unsplash.com).
To send images to the Amazon Bedrock API we need to need to encode them as `base64` strings. Create the following helper methods:
`
1
def readFileAsBase64(file_path):
2
  """Encode image as base64 string."""
3
  try:
4
    with open(file_path, "rb") as image_file:
5
      input_image = base64.b64encode(image_file.read()).decode("utf8")
6
    return input_image
7
  except:
8
    print("bad file name")
9
    sys.exit(0)
101112
def construct_bedrock_image_body(base64_string):
13
  """Construct the request body.
1415
  https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-mm.html
16
  """
17
  return json.dumps(
18
    {
19
      "inputImage": base64_string,
20
      "embeddingConfig": {"outputEmbeddingLength": 1024},
21
    }
22
  )
232425
def get_embedding_from_titan_multimodal(body):
26
  """Invoke the Amazon Titan Model via API request."""
27
  response = bedrock_client.invoke_model(
28
    body=body,
29
    modelId="amazon.titan-embed-image-v1",
30
    accept="application/json",
31
    contentType="application/json",
32
  )
3334
  response_body = json.loads(response.get("body").read())
35
  print(response_body)
36
  return response_body["embedding"]
373839
def encode_image(file_path):
40
  """Generate embedding for the image at file_path."""
41
  base64_string = readFileAsBase64(file_path)
42
  body = construct_bedrock_image_body(base64_string)
43
  emb = get_embedding_from_titan_multimodal(body)
44
  return emb
`
Next, create a `seed` method, which will create a new Supabase Vector Collection, generate embeddings for your images, and upsert the embeddings into your database:
`
1
def seed():
2
  # create vector store client
3
  vx = vecs.create_client(DB_CONNECTION)
45
  # get or create a collection of vectors with 1024 dimensions
6
  images = vx.get_or_create_collection(name="image_vectors", dimension=1024)
78
  # Generate image embeddings with Amazon Titan Model
9
  img_emb1 = encode_image('./images/one.jpg')
10
  img_emb2 = encode_image('./images/two.jpg')
11
  img_emb3 = encode_image('./images/three.jpg')
12
  img_emb4 = encode_image('./images/four.jpg')
1314
  # add records to the *images* collection
15
  images.upsert(
16
    records=[
17
      (
18
        "one.jpg",    # the vector's identifier
19
        img_emb1,    # the vector. list or np.array
20
        {"type": "jpg"} # associated metadata
21
      ), (
22
        "two.jpg",
23
        img_emb2,
24
        {"type": "jpg"}
25
      ), (
26
        "three.jpg",
27
        img_emb3,
28
        {"type": "jpg"}
29
      ), (
30
        "four.jpg",
31
        img_emb4,
32
        {"type": "jpg"}
33
      )
34
    ]
35
  )
36
  print("Inserted images")
3738
  # index the collection for fast search performance
39
  images.create_index()
40
  print("Created index")
`
Add this method as a script in your `pyproject.toml` file:
`
1
[tool.poetry.scripts]
2
seed = "image_search.main:seed"
3
search = "image_search.main:search"
`
After activating the virtual environtment with `poetry shell` you can now run your seed script via `poetry run seed`. You can inspect the generated embeddings in your Supabase Dashboard by visiting the [Table Editor](https://supabase.com/dashboard/project/_/editor), selecting the `vecs` schema, and the `image_vectors` table.
## Perform an image search from a text query[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#perform-an-image-search-from-a-text-query)
With Supabase Vector we can easily query our embeddings. We can use either an image as the search input or alternatively we can generate an embedding from a string input and use that as the query input:
`
1
def search(query_term: Optional[str] = None):
2
  if query_term is None:
3
    query_term = sys.argv[1]
45
  # create vector store client
6
  vx = vecs.create_client(DB_CONNECTION)
7
  images = vx.get_or_create_collection(name="image_vectors", dimension=1024)
89
  # Encode text query
10
  text_emb = get_embedding_from_titan_multimodal(json.dumps(
11
    {
12
      "inputText": query_term,
13
      "embeddingConfig": {"outputEmbeddingLength": 1024},
14
    }
15
  ))
1617
  # query the collection filtering metadata for "type" = "jpg"
18
  results = images.query(
19
    data=text_emb,           # required
20
    limit=1,              # number of records to return
21
    filters={"type": {"$eq": "jpg"}},  # metadata filters
22
  )
23
  result = results[0]
24
  print(result)
25
  plt.title(result)
26
  image = mpimg.imread('./images/' + result)
27
  plt.imshow(image)
28
  plt.show()
`
By limiting the query to one result, we can show the most relevant image to the user. Finally we use `matplotlib` to show the image result to the user.
That's it, go ahead and test it out by running `poetry run search` and you will be presented with an image of a "bike in front of a red brick wall".
## Conclusion[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#conclusion)
With just a couple of lines of Python you are able to implement image search as well as reverse image search using the Amazon Titan multimodal model and Supabase Vector.
## More Supabase[#](https://supabase.com/blog/semantic-image-search-amazon-bedrock#more-supabase)
  * [Getting started with Amazon Bedrock and vecs](https://supabase.com/docs/guides/ai/integrations/amazon-bedrock)
  * [Matryoshka embeddings: faster OpenAI vector search using Adaptive Retrieval](https://supabase.com/blog/matryoshka-embeddings)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&t=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)
[Last postAnnouncing Data Preservation Service1 April 2024](https://supabase.com/blog/pg-paper-dump)
[Next postPostgREST Aggregate Functions29 February 2024](https://supabase.com/blog/postgrest-aggregate-functions)
[postgres](https://supabase.com/blog/tags/postgres)[developers](https://supabase.com/blog/tags/developers)[AI](https://supabase.com/blog/tags/AI)
On this page
  * [Create a new Python project with Poetry](https://supabase.com/blog/semantic-image-search-amazon-bedrock#create-a-new-python-project-with-poetry)
  * [Spin up a Postgres Database with pgvector](https://supabase.com/blog/semantic-image-search-amazon-bedrock#spin-up-a-postgres-database-with-pgvector)
  * [Install the dependencies](https://supabase.com/blog/semantic-image-search-amazon-bedrock#install-the-dependencies)
  * [Import the necessary dependencies](https://supabase.com/blog/semantic-image-search-amazon-bedrock#import-the-necessary-dependencies)
  * [Create embeddings for your images](https://supabase.com/blog/semantic-image-search-amazon-bedrock#create-embeddings-for-your-images)
  * [Perform an image search from a text query](https://supabase.com/blog/semantic-image-search-amazon-bedrock#perform-an-image-search-from-a-text-query)
  * [Conclusion](https://supabase.com/blog/semantic-image-search-amazon-bedrock#conclusion)
  * [More Supabase](https://supabase.com/blog/semantic-image-search-amazon-bedrock#more-supabase)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&text=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsemantic-image-search-amazon-bedrock&t=Implementing%20semantic%20image%20search%20with%20Amazon%20Titan%20and%20Supabase%20Vector)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)
  * [AI Builders](https://supabase.com/solutions/ai-builders)


###### Resources
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets / Logos](https://supabase.com/brand-assets)
  * [Security and Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Blog](https://supabase.com/blog)
  * [Customer Stories](https://supabase.com/customers)
  * [Careers](https://supabase.com/careers)
  * [Company](https://supabase.com/company)
  * [Events & Webinars](https://supabase.com/events)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme

