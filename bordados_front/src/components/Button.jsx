function Button(props) {
    return <button onClick={props.onClick} className={`btn btn-${props.variant} ${props.className} d-flex flex-row justify-content-center gap-2`}>
        {
            props.icon ?
            <i className={`bi bi-${props.icon}`}></i>
            : ""
        }
        {props.children}
    </button>
}

export default Button;