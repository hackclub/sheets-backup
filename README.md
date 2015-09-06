# sheets-backup

Back up a Google Sheet to a git repository.

## Usage

Prerequisites:

- LibreOffice
- Git

Set the following environment variables:

- `GIT_REMOTE` - Remote of the git repository to push to. If the repo requires
  authentication, include the username and password in the URL (ex.
  `https://username:password@github.com/repo.git`) Note: this repo will be
  pulled from on first start.
- `GIT_COMMITTER_NAME` - Full name to make commits under. Ex. "Zaphod
  Beeblebrox"
- `GIT_COMMITTER_EMAIL` - Email to make commits under. Ex.
  "zaphod@beeblebrox.com"

## License

See [LICENSE](LICENSE).
