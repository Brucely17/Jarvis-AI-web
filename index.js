const express=require('express')
const {exec}=require('child_process')
const path=require('path')
const value=''
const pythonScript="speechrecog.py";
const pythonProcess = exec(`python ${pythonScript}`, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing Python script: ${error}`);
        return;
    }

    if (stderr) {
        console.error(`Python script produced an error: ${stderr}`);
        return;
    }

    // Python script output
    const lines = stdout.split('\n');
    lines.forEach((line) => {
        if (line.startsWith("MyText = ")) {
            const value = line.split('=')[1].trim();
            console.log(`Value of my_variable: ${value}`);
        }
    });
    console.log(`Python Output: ${stdout}`);
});

const app=express()


app.get('/value',(req,res)=>{
    res.send(value)
    console.log(value)
})
app.post('')
app.listen(8080,console.log("Connecte to port 8080"))

