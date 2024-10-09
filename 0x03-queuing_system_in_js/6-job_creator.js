const kue = require('kue');

const queue = kue.createQueue();
const jobInfo = {
	phoneNumber: '1234567890',
	message: 'notification',
};

const job = queue.create('push_notification_code', jobInfo)
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  })
  .save((err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('Notification job created: '+ job.id);
    }
  });
