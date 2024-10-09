/**
 * 0-redis_client.js, It should connect to the Redis server running
 */
import { createClient } from 'redis';

const client = createClient();
const Kill = ('KILL_SERVER');
//The console should log a message, when the connection to Redis works
//correctly
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

//The console should log a message, when the connection to Redis does not work
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ' + err);
});

client.on('message', (err, message) => {
  console.log(`${message}`);

  if (message === Kill) {
    client.unsubscribe();
    client.quit();
  }
});
