---
url: https://supabase.com/blog/supabase-nft-marketplace
scraped_at: 2025-05-25T09:33:49.077539
title: Supabase Launches NFT Marketplace
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
# Supabase Launches NFT Marketplace
01 Apr 2021
•
3 minute read
[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Ant WilsonCTO and Co-Founder](https://github.com/awalias)
![Supabase Launches NFT Marketplace](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnft%2Fnft-3.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Crypto at Supabase[#](https://supabase.com/blog/supabase-nft-marketplace#crypto-at-supabase)
Most people don’t know this but the Supabase team has a long history of involvement in the NFT game. In 2018, [Copple](https://www.blockpunk.net/en/collection/paul-copplestone) and [Rory](https://www.blockpunk.net/en/collection/rory-wilding) were minted as NFTs on [Blockpunk.net](https://www.blockpunk.net), an Ethereum based Anime-NFT platform that four Supabase core team members helped build. We also helped in the building of the world’s first tokenised anime premiere - [Vevara in Your Dream](https://www.animationmagazine.net/anime/first-tokenized-anime-film-vevara-in-your-dream-debuts/).
The team were also founding members of the [Guacchain Foundation](https://github.com/awalias/guacchain), an economic experiment in a deflationary-based monetary system, inspired by the fact that Avacados ripen faster when stored together.
NFTs are now capturing the imagination of speculators everywhere, but NFTs as they exist today have a major flaw. We call it the _Copy-Paste Problem_. The Copy-Paste problem is when a token contains a URL to an image hosted on the web, or even on IPFS; there is nothing stopping someone who does not own the token, from heading to that URL, and just downloading the image for themselves.
As our latest foray into NFTs we’re announcing [BuyMeth.com](https://buymeth.com/), (Meth = [M]isleading [E]ncrypted [Th]umbnails) an NFT marketplace that solves the copy-paste problem of NFTs today.
![Supabase NFT marketplace BuyMeth.com](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnft%2Fnft-1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### How does it work?[#](https://supabase.com/blog/supabase-nft-marketplace#how-does-it-work)
Each NFT stores a blurhash representation of a full image, but also a link to the full encrypted version of the image stored on IPFS. The full image is always encrypted with the key of the _current_ owner.
When a sale is initiated i.e. the seller accepts a buyers offer, Metamask re-encrypts the image with the public key of the buyer, and uploads it to IPFS, the url in the NFT is updated and the buyer assigned as the new owner. After the sale, a 1 week challenge period is initiated where the proceeds of the sale are kept in an escrow contract. The buyer can then decrypt the contents of the image, and can run an automated verification function to verify that the image received (when hashed) does indeed produce the publically available blurhash (or thumbnail). If it does not, then the buyer can submit a claim to the sales contract, along with a proof of the invalid file, and claim back the proceeds.
![Most popular NFTs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fnft%2Fnft-2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
As a way to dis-incentivise previous owners of the image to not reveal the original image, we bake in a royalty mechanism, whereby previous owners receive a fraction of the sale price each time, the artwork changes hands.
Despite the undeniable value of such a platform, this announcement is of course an April Fools joke. We are not launching a Supabase NFT platform; but we are [Launching a TON of other stuff this week](https://supabase.com/blog/launch-week).
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&t=Supabase%20Launches%20NFT%20Marketplace)
[Last postWorkflows are coming to Supabase2 April 2021](https://supabase.com/blog/supabase-workflows)
[Next postSupabase CLI31 March 2021](https://supabase.com/blog/supabase-cli)
[supabase](https://supabase.com/blog/tags/supabase)[nfts](https://supabase.com/blog/tags/nfts)
On this page
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&text=Supabase%20Launches%20NFT%20Marketplace)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-nft-marketplace&t=Supabase%20Launches%20NFT%20Marketplace)
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

