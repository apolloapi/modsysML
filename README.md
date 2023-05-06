<div align="center">

![ApolloLogo](https://uploads-ssl.webflow.com/640ca38ad086fde245b76c9d/6455b1fd3d8642575f793c94_header.png)

</div>

<h1 align="center">Open-source Task Automation</h1>

<div align="center">
Apollo is an open-source no-code platform that helps you build automated workflows in minutes. Our SDK allows you to automate tasks such as; onboarding, compliance, trust & safety, fraud detection, code generation and more.
</div>

<p align="center">
    <br />
    <a href="https://docs.apolloapi.io/" rel="dofollow"><strong>Docs »</strong></a>
    <br />

  <br/>
    <a href="https://www.apolloapi.io/">Join the waitlist</a>
    ·
    <a href="https://github.com/apolloapi/apolloapi/issues">Report Bug</a>
    ·
    <a href="https://discord.gg/ZUH7f7AzUY">Community Discord</a>
</p>

## Why Apollo API?

Before Apollo, integrating AI models and building automated workflows could be time-consuming and complex, with Apollo, teams can simplify and accelerate the process, making it easier to deploy AI models, sync data, and develop insights in minutes.

## 🚀 Interesting, how can I try it?

Lets install the SDK first...

```bash
pip install apollo-sdk
```

Let's setup your first Integration!

It will pull from your local database (and keep it in sync).

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

...and create a workflow with a simple command:

_Note: you can obtain a Auth token [here](https://docs.apolloapi.io/docs/api/authentication), sign up today on our [Site](https://app.apolloapi.io/)_

```python
# import the package
from apollo.client import Apollo

# Use our custom model to test building decisions
Apollo.use("apollo", token="YOUR_API_TOKEN_HERE")

# Lets check to see if a phrase contains threats
Apollo.detectText("Phrase1", "contains", "Threats")

# Create custom rules which creates a task!
Apollo.rule('Phrase1', '>=', '0.8')

# Connect with other models!
Apollo.use('Google', "violence", ...)

Apollo.detectImage('Image1', 'contains', 'VERY_LIKELY') # Image Analysis/OCR
Apollo.detectSpeech('Audio1', 'contains', 'UNLIKELY') # Audio Processing
Apollo.detectVideo('Video1', 'contains', 'POSSIBLE') # Video Analysis
Apollo.detectText('Phrase1', 'contains', 'UNKNOWN') # Text Analysis
```

That's all it takes!

## Apollo then takes care of:

- Detecting real-time changes in your data
- Automating tasks against image, video, audio or text
- Simplifying the process of deploying AI models
- Making sure your integration is robust, so you never again have to worry about stuck/stale data or false-positives

In practice, you probably want to use one of our native SDKs to interact with Apollo's API or use our custom browser client so you dont have to write code. If so, sign up at [Apollo API](https://app.apolloapi.io/signup)!

## 🧑‍💻 Cool, what can I build with it?

- Trust & Safety teams can use Apollo to **build native in-app connections** related to active response, content moderation, fraud detection, etc.
- Some **automate their personal lives** with Apollo by integrating against discord communities or their personal lives
- Apollo can help you **quickly automate tasks** for hobby projects, communities or business

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
