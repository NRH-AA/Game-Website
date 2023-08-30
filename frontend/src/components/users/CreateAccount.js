import { useState, useEffect, useCallback } from 'react';



const CreateAccountComponent = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [accountName, setAccountName] = useState('');
    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');
    const [errors, setErrors] = useState({});
    const [submitted, setSubmitted] = useState(false);
    
    const [accounts, setAccounts] = useState(false);
    
    const validateData = useCallback(() => {
        const newErrors = {};
        
        if (!username || (username.length < 4 || username.length > 20)) newErrors.username = 'Username must be 4-20 characters.';
        if (!email || (email.length < 4 || email.length > 50)) newErrors.email = 'Email must be 4-50 characters.';
        if (!accountName || (accountName.length < 4 || accountName.length > 20)) newErrors.accountName = 'Account name must be 4-20 characters.';
        if (!password || (password.length < 4 || password.length > 30)) newErrors.password = 'Password must be 4-30 characters.';
        if (!password2 || (password2.length < 4 || password2.length > 30)) newErrors.password2 = 'Password must be 4-30 characters.';
        if (password !== password2) newErrors.password = 'Passwords do not match.'
        
        setErrors(newErrors);
    }, [username, email, accountName, password, password2])
    
    const getAllAccounts = async () => {
        const res = await fetch('/api/account/');
        
        if (res.ok) {
            const data = await res.json();
            return setAccounts(data.accounts);
        }
        
        return setAccounts([]);
    };
    
    
    useEffect(() => {
        if (submitted) validateData();
    }, [validateData, submitted, username, email, accountName, password, password2]);
    
    useEffect(() => {
        if (!accounts) getAllAccounts();
    }, [accounts]);
    
    
    const createAccount = async () => {
        const res = await fetch('/api/account', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: accountName,
                email,
                username,
                password,
                confirmPassword: password2
            })
        });
        
        
        if (res.ok) {
            const data = await res.json();
            if (data.error) setErrors({username: data.error});
            if (data.success) setErrors({username: data.success});
        };
    };
    
    const handleSubmit = (e) => {
        e.preventDefault();
        
        setSubmitted(true);
        validateData();
        
        if (Object.keys(errors).length > 0) return;
        
        console.log('Creating Account');
        return createAccount();
    }
    
    return (
        <div id='create-account-container'
            style={{
                marginTop: '20px',
                display: 'flex', 
                flexDirection: 'column', 
                alignItems: 'center', 
                gap: '10px'
            }}
        >
            
            <div>
                {accounts?.length ? accounts.map((el, i) =>
                    <p key={i}>{el.name} {el.creation} {el.email}</p>
                )
                : null
                }
            </div>
            
            
            {errors?.username && <p>{errors.username}</p>}
            <input type='text' placeholder='Username'
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            
            {errors?.accountName && <p>{errors.accountName}</p>}
            <input type='text' placeholder='Account Name'
                value={accountName}
                onChange={(e) => setAccountName(e.target.value)}
            />
            
            {errors?.email && <p>{errors.email}</p>}
            <input type='email' placeholder='Email'
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            
            {errors?.password && <p>{errors.password}</p>}
            <input type='password' placeholder='Password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            
            {errors?.password2 && <p>{errors.password2}</p>}
            <input type='password' placeholder='Confirm Password'
                value={password2}
                onChange={(e) => setPassword2(e.target.value)}
            />
            
            <button type='button'
                onClick={handleSubmit}
            >Create</button>
        </div>
    );
};

export default CreateAccountComponent;
