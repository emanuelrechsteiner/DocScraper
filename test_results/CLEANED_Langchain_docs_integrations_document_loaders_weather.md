On this page
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/langchain-ai/langchain/blob/master/docs/docs/integrations/document_loaders/weather.ipynb)[![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)](https://github.com/langchain-ai/langchain/blob/master/docs/docs/integrations/document_loaders/weather.ipynb)
# Weather
This loader fetches the weather data from the OpenWeatherMap's OneCall API, using the pyowm Python package. You must initialize the loader with your OpenWeatherMap API token and the names of the cities you want the weather data for.
```
from langchain_community.document_loaders import WeatherDataLoader
```

**API Reference:**[WeatherDataLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.weather.WeatherDataLoader.html)
```
%pip install --upgrade --quiet pyowm
```

```
# Set API key either by passing it in to constructor directly# or by setting the environment variable "OPENWEATHERMAP_API_KEY".from getpass import getpassOPENWEATHERMAP_API_KEY = getpass()
```

```
loader = WeatherDataLoader.from_params(["chennai","vellore"], openweathermap_api_key=OPENWEATHERMAP_API_KEY)
```

```
documents = loader.load()documents
```

## Related[​](https://python.langchain.com/docs/integrations/document_loaders/weather/#related "Direct link to Related")
  * Document loader [conceptual guide](https://python.langchain.com/docs/concepts/document_loaders/)
  * Document loader [how-to guides](https://python.langchain.com/docs/how_to/#document-loaders)


[Edit this page](https://github.com/langchain-ai/langchain/edit/master/docs/docs/integrations/document_loaders/weather.ipynb)
#### Was this page helpful?

  * [Related](https://python.langchain.com/docs/integrations/document_loaders/weather/#related)


Community
  * [Twitter](https://twitter.com/LangChainAI)


GitHub
  * [Organization](https://github.com/langchain-ai)
  * [Python](https://github.com/langchain-ai/langchain)
  * [JS/TS](https://github.com/langchain-ai/langchainjs)


More
  * [Homepage](https://langchain.com)
  * [Blog](https://blog.langchain.dev)
  * [YouTube](https://www.youtube.com/@LangChain)