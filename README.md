<div align="center">

![ApolloLogo](https://uploads-ssl.webflow.com/640ca38ad086fde245b76c9d/643fffb82419ac18d39e3e4e_Screenshot%202023-04-19%20at%2010.50.13%20AM.png)

</div>

<h1 align="center">The easiest way to build custom decision making workflows</h1>

<div align="center">
Apollo gives you access to custom machine learning models, no-code platform and continuously syncs data from any API or Database to centralize investigations and allow you to automate the detection of harm in images, videos, audio and text.
</div>

<p align="center">
    <br />
    <a href="https://apolloapi.io" rel="dofollow"><strong>Docs coming soon »</strong></a>
    <br />

  <br/>
    <!-- <a href="https://docs.nango.dev">Examples</a> -->
    <a href="https://www.apolloapi.io/">Join the waitlist</a>
    ·
    <a href="https://github.com/apolloapi/apolloapi/issues">Report Bug</a>
    ·
    <a href="https://discord.gg/ZUH7f7AzUY">Community Discord</a>
</p>

## ⭐ Can you show me an example?

In your code you can write:

```ts
Apollo.connect('postgres://username:password@hostnam...', ...) // Starts syncing content forever!

Apollo.use('OpenAI', "moderation", ...) // Connect to existing providers!

Apollo.rule('Phrase1', '>=', '0.8') // Create custom rules!

Apollo.use('Apollo', "violence", ...) // Connect with our internal models!

// Detect bad actors at scale!
Apollo.detectImage('Image1', 'contains', 'VERY_LIKELY') // Image Analysis/OCR
Apollo.detectSpeech('Audio1', 'contains', 'UNLIKELY') // Audio Processing
Apollo.detectVideo('Video1', 'contains', 'POSSIBLE') // Video Analysis
Apollo.detectText('Phrase1', 'contains', 'UNKNOWN') // Text Analysis

```

Apollo then takes care of:

- Detecting real-time changes in user experience
- Automated detection against image, video, audio or text
- Connecting policy to product
- Making sure your integration is robust, so you never again have to worry about stuck/stale data or false-positives

## 🧑‍💻 Cool, what can I build with it?

- Trust & Safety teams in companies use Apollo to **build native in-app connections** related to active response, content moderation, fraud detection, etc.
- Some **automate their personal lives** with Apollo by integrating against discord communities or other decentralized networks for safety
- Apollo can help you **quickly build trust** for hobby projects, communities or business

## 🚀 Interesting, how can I try it?

Let's setup your first Integration in 2 minutes!

It will pull from your local database (and keep it in sync).

Test sending your content to our API!

...and create a Integration with a simple command:

```bash
pip install
```

```python

```

That's all it takes!

That's all it takes! You can check out [the list of all Pokémons in your local database](http://localhost:8080/?pgsql=nango-db&username=nango&db=nango&ns=public&select=_nango_raw) (password is `nango`).

In practice, you probably want to use one of our native SDKs to interact with Apollo's API or use our custom browser client so you dont have to write code.

```js
import { Nango } from "@nangohq/node-client";
let config = {
  response_path: "results", // The path to the Pokémons objects in the response.
  paging_url_path: "next", // The path to the next page's url in the response.
};
await Nango.sync("https://pokeapi.co/api/v2/pokemon", config);
```

## Contributing

### 📦 pre-commit config

Clone the repo and start Apollo locally...

```bash
git clone https://github.com/apolloapi/apolloapi.git
cd apolloapi && python3 -m venv env && source env/bin/activate && pip install -r requirements.txt
```

- After installing system dependencies be sure to install pre-commit for lint checks

```bash
pip install pre-commit

pre-commit install

pre-commit run --all-files
```

## 🔍 Neat, I would like to learn more

⭐ Follow our development by starring us here on GitHub ⭐

<!-- - Explore some [Real world examples](https://www.thebriefnewsletter.com) -->

- Share feedback or ask questions on the [Discord community](https://discord.gg/ZUH7f7AzUY)
- [Chat with a member of the team](https://apolloapi.io) 👋
- Check our [blog on Trust & Safety](https://www.thebriefnewsletter.com)
