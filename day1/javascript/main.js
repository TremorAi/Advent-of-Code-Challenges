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
    let lines = [];
    const rl = readline.createInterface({
      input: fs.createReadStream(filePath),
      crlfDelay: Infinity
    });
    rl.setMaxListeners(5000);
    rl.on("line", line => {
      lines.push(line);
    });
    rl.on("close", () => {
      var num = 0;
      while (thang) {
        for (let line of lines) {
          num += parseInt(line);
          if (listthing.has(num)) {
            console.log("HELP?");
            thang = false;
            event.sender.send("fileData", num);
            break;
          } else {
            listthing.add(num);
          }
        }
      }
    });
  }
});
app.on("ready", createWindow);
