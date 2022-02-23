try {
    const file = 'script.txt'
    const content = msg.content.replace(prefix, '').replace(command + ' ', '')
    try {
        fs.writeFileSync(file, content)
    } catch (err) {
        console.log('An error ocurred: ' + err)
    }
    const {
        exec
    } = require("child_process");

    exec("python 1.py", (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log('Output: ' + stdout)
    });
} catch (e) {
    console.log('An error ocurred: ' + e)
}
