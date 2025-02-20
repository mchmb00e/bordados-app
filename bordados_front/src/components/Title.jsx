function Title(props) {
    return <h1 className={`${ props.fontSize ? "fs-"+props.fontSize : "" }`}>Bordados<b className="text-primary">App</b></h1>
}

export default Title;