const express = require('express');
const expressWs = require('express-ws')
const router = express.Router()
expressWs(router);
let wSocket

router.ws('/event-logs-stream', (ws, req) => {
    console.log("event-logs-stream-route");
    wSocket = ws;
})

// import the `Kafka` instance from the kafkajs library
const { Kafka } = require("kafkajs")
// the client ID lets kafka know who's producing the messages
const clientId = "event-logs"
// we can define the list of brokers in the cluster
const brokers = ["kafka-server:9092"]
// this is the topic to which we want to write messages
const topic = "event-logs-stream"

// initialize a new kafka client and initialize a producer from it
const kafka = new Kafka({ clientId, brokers })

const consumer = kafka.consumer({ groupId: clientId })

const consume = async () => {
	// first, we wait for the client to connect and subscribe to the given topic
	await consumer.connect()
	await consumer.subscribe({ topic })
	await consumer.run({
		// this function is called every time the consumer gets a new message
		eachMessage: ({ message }) => {
			// here, we just log the message to the standard output
			console.log(`received message: ${message.value}`)
			if (wSocket != undefined)
        		wSocket.send(JSON.stringify(message))
		},
	})
}

consume().catch((err) => {
    console.error("Something went wrong with our consumer");
})


module.exports = router