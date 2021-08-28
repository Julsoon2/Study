const { request } = require('express');
const express = require('express');
const app = express();

app.listen(8080, function(){
    console.log('listening on 8080')
});


app.get('/', function(req, res){ //request 요청, response 응답
    res.sendFile(__dirname + '/index.html');
});