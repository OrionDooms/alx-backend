/**
 * 0-redis_client.js, It should connect to the Redis server running
 */
import { createClient } from 'redis';

const client = createClient();

//The console should log a message, when the connection to Redis does not work
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

//The console should log a message, when the connection to Redis works
//correctly
client.on('connect', () => {
  console.log('Redis client connected to the server');

  client.hset('HolbertonSchools', 'Portland' , 50, (err, reply) => {
    if (err) console.error(err);
    console.log('Reply:', reply === 'Portland' ? 0 : 1);
  });
  client.hset('HolbertonSchools', 'Seattle' , 80, (err, reply) => {
    if (err) console.error(err);
    console.log('Reply:', reply === 'Seattle' ? 0 : 1);
  });
  client.hset('HolbertonSchools', 'New York' , 20, (err, reply) => {
    if (err) console.error(err);
    console.log('Reply:', reply === 'New York' ? 0 : 1);
  });
  client.hset('HolbertonSchools', 'Bogota' , 20, (err, reply) => {
    if (err) console.error(err);
    console.log('Reply:', reply === 'Bogota' ? 0 : 1);
  });
  client.hset('HolbertonSchools', 'Cali' , 40, (err, reply) => {
    if (err) console.error(err);
    console.log('Reply:', reply === 'Cali' ? 0 : 1);
  });
  client.hset('HolbertonSchools', 'Paris' , 2, (err, reply) => {
    if (err) console.error(err);
    console.log('Reply:', reply === 'Paris' ? 0 : 1);
  });
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) console.error(err);
    console.log('Hash:', reply);
  });
});
