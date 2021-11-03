# Contributing

Thank you for investing your time in contributing to our project! Any contribution you make will be reflected on [https://www.hommmer.org/](https://www.hommmer.org/).

## New contributor guide

See the [README](README.md) to get an overview of the project. Ideas for improvement are in [TODO](TODO.md). We're operating under the MIT Open Source [license](LICENSE) so you can still use anything you contribute (but so can the rest of us).

## Getting started

### Issues

#### Create a new issue

If you spot a problem with the docs, [search if an issue already exists](https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-issues-and-pull-requests#search-by-the-title-body-or-comments). If a related issue doesn't exist, you can open a [new issue](https://github.com/hammer-mt/hommmer/issues/new).

#### Solve an issue

Scan through our [existing issues](https://github.com/hammer-mt/hommmer/issues) to find one that interests you. Leave a comment on the issue asking if you can pick up the issue so maintainers knowing you want to work on it.

### Make Changes

#### Prerequisites

Make sure you have the following installed in your development environment:

- [Python](https://www.python.org/downloads/)

#### Development Workflow

Follow these steps below to get the package working locally:

1. Create a personal fork of the project on GitHub and clone locally

```shell
# Using HTTPS
git clone https://github.com/your-username/hommmer.git

# Or using SSH
git clone git@github.com:your-username/hommmer.git
```

2. Add the original repository as a remote called `upstream`

```shell
git remote add upstream https://github.com/hammer-mt/hommmer.git
```

3. Make sure to pull upstream changes into your local repository

```shell
git fetch upstream
```

4. Create a new branch to work from

```shell
git checkout -b branchname
```

5. Activate a virtual environment

```shell
python -m venv venv

# Using Windows
`venv\Scripts\activate`

# Using Mac
`source ./venv/bin/activate`
```

6. Install the package as editable

```shell
# Install from the cloned repo:
%pip install -e your/local/path
```

I like working from Jupyter Notebook (Anaconda) because if you run `%loadext autoreload` then `%aimport hommmer` the module will auto-reload on every saved change to your local package.

7. Make your changes / contributions

Make sure to follow the code style of the project, run any tests (if available) and add / update the documentation as needed.

Squash your commits with git's [interactive rebase](http://git-scm.com/docs/git-rebase) (create a new branch if necessary). Write your commit messages in the present tense (what does it does to the code?). Push your changes to your fork on GitHub, the remote `origin`.

```shell
# Squash commits, fix up commit messages etc.
git rebase -i origin/main

# Push to your fork on GitHub
git push origin main
```

### Pull Request

When you're done making the changes, open a pull request, often referred to as a PR. You do this in GitHub from your Fork of the project. Target the `develop` branch if there is one, else go for `main`.

- Fill out the PR description summarizing your changes so we can review your PR. This template helps reviewers understand your changes and the purpose of your pull request.
- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.
- Enable the checkbox to [allow maintainer edits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork) so the branch can be updated for a merge. Once you submit your PR, a Docs team member will review your proposal. We may ask questions or request for additional information.
- We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.
- As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).
- If you run into any merge issues, checkout this [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) to help you resolve merge conflicts and other issues.
- Once the pull request is approved and merged you can pull the changes from upstream to your local repo and delete your extra branch(es).

### Your PR is merged!

Congratulations :tada::tada: The hommmer team thanks you!

Once your PR is merged, we will add you to the All Contributors Table in the [`README.md`](./README.md#all-contributors)
