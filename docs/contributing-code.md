# Contributing

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

#### Accepted `<type>` values:

- new = newly implemented user-facing features
- chg = changes in existing user-facing features
- fix = user-facing bugfixes
- oth = other changes which users should know about
- dev = any developer-facing changes, regardless of new/chg/fix status

#### Summary (The first line)

The first line should not be longer than 75 characters, the second line is always blank and other lines should be wrapped at 80 characters.
