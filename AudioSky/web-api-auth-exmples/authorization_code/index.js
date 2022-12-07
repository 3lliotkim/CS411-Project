const express = require('express');
const morgan = require('morgan');
const { Prohairesis } = require('prohairesis');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 8888;

const mySQLString='mysql://bd44e301068fc3:bd6016d1@us-cdbr-east-06.cleardb.net/heroku_481ef6d2cb7d903?reconnect=true';
const database = new Prohairesis(mySQLString);

app
    .use(morgan('dev'))    
    .use(express.static('public'))
    
    .use(bodyParser.urlencoded({ extended: false }))
    .use(bodyParser.json())

    .post('/api/user', async (req, res) => {
        const body = req.body;

        await database.execute(`
            INSERT INTO User (
                user_email
            ) VALUES (
                @userEmail
            )
        `, {
            userEmail: body.email
        });

        res.end('Added email');
    })

    .listen(port, () => console.log(`Server listening on port ${port}`));