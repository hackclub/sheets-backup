function initiateGitBackup () {
  var token = ScriptApp.getOAuthToken();
  var ssID = SpreadsheetApp.getActiveSpreadsheet().getId();
  var options = {
    "method": "post",
    "payload": {
      "access_token": token,
      "spreadsheet_id": ssID
    }
  };

  UrlFetchApp.fetch("https://example.com/initiate_backup", options);
}
