
function loginPage(){
    return (
        <div>
            <form>
                <h1>Log in</h1>
                <label>Email</label>
                <input type='email' placeholder='email' /><br></br>
                <label>Password</label>
                <input type='password' placeholder='password'/>
                <a href="#">Forgot your password?</a><br/>
            <a href="#">Don't have an account?</a>
            </form>
        </div>
    )
}

export default loginPage