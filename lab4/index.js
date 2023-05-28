const { program } = require('commander');
const fs = require('fs');
const tasksFile = './tasks.json';

let tasks = [];

program.description('An application to track tasks');

program
  .command('add <title>')
  .description('Add a new task')
  .option('-d, --description [description]', 'Add description to the task')
  .action((title, options) => {
    const task = {
      title,
      description: options.description || '',
    };
    tasks.push(task);
    fs.writeFileSync(tasksFile, JSON.stringify(tasks));
  });

program.parse(process.argv);