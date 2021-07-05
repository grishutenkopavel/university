const http = require('http');

http.createServer((request, response) => {
    if(process.env.NODE_ENV=='prodaction'){
        response.end(request.url);
    } else if (process.env.NODE_ENV=='debug'){
        response.end(request.url.split("").reverse().join(""));
    }
    
    
}).listen(process.env.PORT || 3000);