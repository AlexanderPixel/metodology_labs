const { program } = require('commander');
const fs = require('fs');
const tasksFile = './tasks.json';

let tasks = [];

if (fs.existsSync(tasksFile)) {
    const tasksJson = fs.readFileSync(tasksFile);
    try {
        tasks = JSON.parse(tasksJson);
    } catch (ex) { }
}

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

  program
  .command('list')
  .description('List all tasks')
  .action(() => {
    console.log(tasks);
  });

program.parse(process.argv);