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
    });
    numthing = 0;
  }
});
