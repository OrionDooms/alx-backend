/**
 * 0-redis_client.js, It should connect to the Redis server running
 */
import { createClient, print } from 'redis';

const client = createClient();
//The console should log a message, when the connection to Redis does not work
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
//The console should log a message, when the connection to Redis works
//correctly
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
