var express = require("express"),
    app = express(),
    bodyParser = require("body-parser"),
    mongoose = require("mongoose"),
    MongoClient = require('mongodb').MongoClient;

var url = "mongodb://giscledb:giscle#123@ds341847.mlab.com:41847/giscle"

const dbName = 'giscle';
// MongoClient.connect(url, { useNewUrlParser: true }, (err, client) => {
//     console.log("Connected successfully to server");
//     dbo = client.db(dbName);
//     dbo.collection('person').find({}).toArray(function (err, docs) {
//         if(err) throw err;
//         console.log(docs)
//     });
//     //   client.close();
// });

app.get("/", (req, res) => {
    res.json("wlcm")
})

app.get("/allperson", (req, res) => {
    MongoClient.connect(url, { useNewUrlParser: true }, (err, client) => {
        console.log("Connected successfully to server");
        dbo = client.db(dbName);
        var data = dbo.collection('person').find({}).toArray(function (err, docs) {
            if(err) throw err;
            // console.log(docs)
            res.send(docs);
        });
    });
})

app.listen(8080, function () {
    console.log("Server has started");
});