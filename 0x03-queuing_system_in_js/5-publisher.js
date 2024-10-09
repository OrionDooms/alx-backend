/**
 * 0-redis_client.js, It should connect to the Redis server running
 */
import { createClient, print } from 'redis';

const client = createClient();
//The console should log a message, when the connection to Redis does not work

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ' + err);
});

//The console should log a message, when the connection to Redis works
//correctly
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
