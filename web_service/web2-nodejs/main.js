const http = require('http'); // 모듈 임포트는 require로. ES6부터는 import로 가능
const fs = require('fs'); // filesystem 모듈
const url = require('url');

function templateHTML(title, list, body) {
    return `
    <!doctype html>
    <html>
    <head>
    <title>WEB1 - ${title}</title>
    <meta charset="utf-8">
    </head>
    <body>
    <h1><a href="/">WEB</a></h1>
    ${list}
    ${body}
    </body>
    </html>
    `
}
function templateList(filelist) {
    let list = '<ul>'
    let i = 0;
    while (i < filelist.length) {
        list = list + `<li><a href="/?id=${filelist[i].slice(0, -4)}">${filelist[i].slice(0, -4)}</a></li>`
        i = i + 1;
    }
    list = list + '</ul>'
    return list
}

const server = http.createServer(function (request, response) {
    let _url = request.url;
    let queryData = url.parse(_url, true).query;
    let pathname = url.parse(_url, true).pathname;

    if (pathname === '/') {
        if (queryData.id === undefined) {
            fs.readdir('./data', function (error, filelist) {
                let title = 'Welcome';
                let description = 'Hello, Home';

                let list = templateList(filelist);
                let template = templateHTML(title, list, `<h2>${title}</h2><p>${description}</p>`)
                response.writeHead(200);
                response.end(template);
            })
        } else {
            fs.readdir('./data', function (error, filelist) {
                fs.readFile(`data/${queryData.id}.txt`, 'utf-8', function (err, description) {
                    let title = queryData.id;
                    let list = templateList(filelist);
                    let template = templateHTML(title, list, `<h2>${title}</h2><p>${description}</p>`);
                    response.writeHead(200);
                    response.end(template);
                });
            });
        }
    } else {
        response.writeHead(404);
        response.end('Not found');
    }



});
server.listen(3000);