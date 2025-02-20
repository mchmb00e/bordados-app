function SelectField(props) {

    return <select className="form-select" onChange={e => props.onChange(e.target.value)}>
            <option value="">Seleccione una categoría</option>
        {
            props.options.map((item) => (
                <option key={item.id} value={item.id}>{item.name}</option>
            ))
        }
    </select>
}

export default SelectField;