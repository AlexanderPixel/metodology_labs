const { program } = require('commander');
const fs = require('fs');
const tasksFile = './tasks.json';

const FEEDBACKS = {
  ERROR: '\x1b[31m%s\x1b[0m',
  SUCCESS: '\x1b[32m%s\x1b[0m',
};

const formatMessage = (str, color) => {
  const message = color.replace('%s', str);
  return message;
}

const handleTaskNotFound = (id) => {
  const error = formatMessage(`Task with id ${id} not found.`, FEEDBACKS.ERROR);
  console.log(error);
}

const handleSuccessfulAction = (str) => {
  const message = formatMessage(str, FEEDBACKS.SUCCESS);
  console.log(message);
}

let tasks = [];

if (fs.existsSync(tasksFile)) {
    const tasksJson = fs.readFileSync(tasksFile);
    try {
      tasks = JSON.parse(tasksJson);
    } catch (ex) { 
      console.error(`Error parsing tasks file: ${ex}`);
    }
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

    handleSuccessfulAction(`Task "${task.title}" was successfully added.`);
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

      handleSuccessfulAction(`Task with id ${id} was successfully deleted.`);
    } else {
      handleTaskNotFound(id);
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

      handleSuccessfulAction(`Task with id ${id} was successfully completed.`);
    } else {
      handleTaskNotFound(id);
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

      handleSuccessfulAction(`Task with id ${id} was successfully edited.`);
    } else {
      handleTaskNotFound(id);
    }
  });

program.parse(process.argv);