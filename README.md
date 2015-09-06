# sheets-backup

Back up a Google Sheet to a git repository.

## Usage

Prerequisites:

- LibreOffice
- Git

_For the server component:_

Set the following environment variables:

- `GIT_REMOTE` - Remote of the git repository to push to. If the repo requires
  authentication, include the username and password in the URL (ex.
  `https://username:password@github.com/repo.git`) Note: this repo will be
  pulled from on first start.
- `GIT_COMMITTER_NAME` - Full name to make commits under. Ex. "Zaphod
  Beeblebrox"
- `GIT_COMMITTER_EMAIL` - Email to make commits under. Ex.
  "zaphod@beeblebrox.com"

Deploy! Everything's already set up for Heroku/Dokku (including the crazy
LibreOffice dependency), if you'd like to use that.

_For the Apps Script component:_

This program works through having an Apps Script attached to a spreadsheet
continually ping an endpoint on the Python server, passing it auth information
and the ID of the spreadsheet to work on.

`script.gs` contains that Apps Script we want to install on our spreadsheet of
choice. To do that, do the following:

1. In your open spreadsheet, click `Tools > Script editor...`.
2. Past the contents of `script.gs` into the default `Code.gs` file (or create a
   new file for this code).
3. Change `example.com` in the pasted code to match the hostname of your
   deployed app.
4. Let's install a trigger to get this script running periodically. While still
   in the script editor, click `Resources > Current project's triggers` and add
   a new time-driven trigger for `initiateGitBackup` and choose an interval that
   works for you. We currently have it running every minute.

Once you've done that, you're good to go!

## License

See [LICENSE](LICENSE).
