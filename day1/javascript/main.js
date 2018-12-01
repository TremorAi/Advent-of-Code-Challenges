const { app, BrowserWindow, dialog } = require("electron");
const url = require("url");
const path = require("path");
const { ipcMain } = require("electron");
let fs = require("fs");
var readline = require("readline");
var stream = require("stream");

var numthing = 0;
var listthing = new Set();
var thang = true;

let win;

function createWindow() {
  win = new BrowserWindow({
    width: 900,
    height: 700
  });

  win.loadURL(
    url.format({
      pathname: path.join(__dirname, "index.html"),
      protocol: "file:",
      slashes: true
    })
  );

  win.openDevTools();
}

ipcMain.on("ondragstart", (event, filePath) => {
  readFile(filePath);

  function readFile(filePath) {
    const rl = readline.createInterface({
      input: fs.createReadStream(filePath),
      crlfDelay: Infinity
    });
    rl.setMaxListeners(5000);
    rl.on("line", line => {
      if (line[0] === "+") {
        var tht = line.slice(1, line.length);
        numthing += Number(tht);
      } else if (line[0] === "-") {
        var tht = line.slice(1, line.length);
        numthing -= Number(tht);
      }
      event.sender.send("fileData", numthing);
      if (line in listthing) {
        thang = false;
        event.sender.send("fileData", numthing);
      } else {
        listthing.add(numthing);
      }

      // console.log(`Line from file: ${line}`);
    });
    numthing = 0;

    // fs.readFile(filepath, "utf-8", (err, data) => {
    //   if (err) {
    //     alert("An error ocurred reading the file :" + err.message);
    //     return;
    //   }
    //   // handle the file content
    //   event.sender.send("fileData", data);
    // });
  }
});

ipcMain.on("clickedbutton", (event, data) => {
  dialog.showSaveDialog(
    { filters: [{ name: "text", extensions: ["txt"] }] },
    function(fileName) {
      if (fileName === undefined) return;
      fs.writeFile(fileName, data, function(err) {});
    }
  );
});
app.on("ready", createWindow);
