const express = require('express');
const expressWs = require('express-ws')
const router = express.Router()
expressWs(router);
const kafka = require('kafka-node'),
    Consumer = kafka.Consumer;
let wSocket

router.ws('/covid-new-cases', (ws, req) => {
    wSocket = ws;
})

client = new kafka.KafkaClient(
    {
        kafkaHost: 'kafka-server:9092',
    }
),
    consumer = new Consumer(
        client,
        [
            { topic: 'covid-new-cases' }
        ],
        {
            autoCommit: false
        }
    );
consumer.on('message', function (message) {
    if (wSocket != undefined)
        wSocket.send(message.value)
});
consumer.on('error', function (err) {
    console.log('error ==> ', err);
});

module.exports = router