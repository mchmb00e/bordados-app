function TextField(props) {
    return <input onChange={(e) => props.onChange(e.target.value)} className={`form-control ${props.className}`} type={props.type} placeholder={props.placeholder}></input>
}

export default TextField;