const { program } = require('commander');
const fs = require('fs');
const tasksFile = './tasks.json';

function formatError(str) {
  return `\x1b[31m${str}\x1b[0m`;
}

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
      id: tasks.length + 1,
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

program
  .command('delete <id>')
  .description('Delete a task')
  .action((id) => {
    const index = tasks.findIndex((t) => t.id === parseInt(id));
    if (index !== -1) {
      tasks.splice(index, 1);
      fs.writeFileSync(tasksFile, JSON.stringify(tasks));
    } else {
      const error = formatError(`Task with id ${id} not found`);
      program.error(error);
    }
  });

program.parse(process.argv);