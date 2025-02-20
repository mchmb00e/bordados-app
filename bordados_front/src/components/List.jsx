import Button from "./Button"

export default function List(props) {

    const handleClick = (e) => {
        props.onClick(e)
    }

    return <ul className="list-group">
        {
            props.content.map((p, index) => (
                <Item key={index} onClick={() => handleClick(index)}
                active={index === props.active ? "active" : ""}
                >{p.name}</Item>
            ))
        }
    </ul>
}

export function Item(props) {
    return <li onClick={e => props.onClick(e)} className={`list-group-item d-flex flex-row justify-content-between align-items-center ${props.active}`}>{ props.children } <span className="d-flex flex-row gap-1">
        <Button variant="primary" icon="eye-fill" />
        <Button variant="primary" icon="trash-fill" />
        </span></li>
}