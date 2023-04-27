<div align="center">

![ApolloLogo](https://uploads-ssl.webflow.com/640ca38ad086fde245b76c9d/643fffb82419ac18d39e3e4e_Screenshot%202023-04-19%20at%2010.50.13%20AM.png)

</div>

<h1 align="center">The easiest way to build custom decision making workflows</h1>

<div align="center">
Apollo gives you access to custom machine learning models, no-code platform and continuously syncs data from any API or Database to centralize investigations and allow you to automate the detection of harm in images, videos, audio and text.
</div>

<p align="center">
    <br />
    <a href="https://apolloapi-doc.vercel.app/" rel="dofollow"><strong>Docs »</strong></a>
    <br />

  <br/>
    <a href="https://apolloapi-doc.vercel.app/">Examples</a>
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

To start:

```bash
# install the cli-toolkit
pip install apollo-sdk

# enter a python repl or create a python file, up to you! (repl is easiest)
python3
```

```python
# import the package
from apollo.client import Apollo

# sync data from your database instance
# (we support supabase at the current moment or postgresql via uri format)
Apollo.connect("postgres://username:password@hostname:port/database_name")

# If you want to test out operation on your external connection
Apollo.fetch_tables()
Apollo.query("desc", "table", "column")
```

Test sending your content to our API!

...and create a workflow with a simple command:

```python
# import the package
from apollo.client import Apollo

# Use our custom model to test building decisions
Apollo.use("Apollo")

# We support video, speech, image and text. Try text!
Apollo.detectText("Phrase1", "contains", "Threats")
```

That's all it takes!

That's all it takes! You can check out [more on our notion page](https://cloudguruab.notion.site/Apollo-e5e347745c1e43798d849d79cce90aba).

In practice, you probably want to use one of our native SDKs to interact with Apollo's API or use our custom browser client so you dont have to write code. If so, ping us at adrian@apolloapi.io!

## Contributing

### 📦 pre-commit config

As an open source project, Apollo welcomes contributions from the community at large. This isn’t an exhaustive reference and is a living document subject to change as needed when the project formalizes any practice or pattern.

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

Apollo uses commit messages for automated generation of project changelog. For every pull request we request contributors to be compliant with the following commit message notation.

```
<type>: <summary>

<body>
```

Accepted `<type>` values:
- new = newly implemented user-facing features
- chg = changes in existing user-facing features
- fix = user-facing bugfixes
- oth = other changes which users should know about
- dev = any developer-facing changes, regardless of new/chg/fix status

#### Summary (The first line)

The first line should not be longer than 75 characters, the second line is always blank and other lines should be wrapped at 80 characters.

## 🔍 Neat, I would like to learn more

⭐ Follow our development by starring us here on GitHub ⭐

- Share feedback or ask questions on the [Discord community](https://discord.gg/ZUH7f7AzUY)
- [Chat with a member of the team](https://apolloapi.io) 👋
- Check our [blog on Trust & Safety](https://www.thebriefnewsletter.com)
- Look at our docs on how to get started [here!](https://apolloapi-doc.vercel.app/)
