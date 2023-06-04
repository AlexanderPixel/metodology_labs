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
  .option('-t, --deadline [deadline]', 'Add deadline to the task')
  .action((title, options) => {
    const task = {
      id: tasks.length + 1,
      title,
      description: options.description || '',
      deadline: new Date(options.deadline) || null,
      completed: false,
      completedDate: null,
    };
    tasks.push(task);
    fs.writeFileSync(tasksFile, JSON.stringify(tasks));
  });

program
  .command('list')
  .description('List all tasks')
  .action(() => {
    console.table(tasks);
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

program
  .command('complete <id>')
  .description('Complete a task')
  .action((id) => {
    const task = tasks.find((t) => t.id === parseInt(id));
    if (task) {
      task.completed = true;
      task.completedDate = new Date();
      fs.writeFileSync(tasksFile, JSON.stringify(tasks));
    }
  });

program
  .command('edit <id>')
  .description('Edit a task')
  .option('-d, --description [description]', 'Edit description of the task')
  .option('-t, --deadline [deadline]', 'Edit the deadline of the task')
  .action((id, options) => {
    const task = tasks.find((t) => t.id === parseInt(id));
    if (task) {
      if (options.description) task.description = options.description;
      if (options.deadline) task.deadline = new Date(options.deadline);
      fs.writeFileSync(tasksFile, JSON.stringify(tasks));
    } 
  });

program.parse(process.argv);