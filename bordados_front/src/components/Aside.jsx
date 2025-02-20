import Title from "./Title";
import Button from "./Button";
import TextField from "./TextField";
import SelectField from "./SelectField";
import List from "./List";
import { useState } from "react";

function Aside(props) {

    const [active, setActive] = useState(null);

    const handleClickItem = (e) => {
        setActive(e)
        props.onClickPattern(e)
    };

  return (
    <div className={props.className}>
      <Title fontSize="3"></Title>
      <div className="d-flex flex-column gap-2">
        <TextField
          type="text"
          placeholder="Buscar..."
          className="border border-2 border-primary rounded-pill"
          onChange={props.onChangeText}
        ></TextField>
        <Button
          icon="star-fill"
          variant="outline-primary"
          className="w-100 border border-2 border-primary"
          onClick={props.onClickFavorites}
        >
          Favoritos
        </Button>
        <SelectField
          onChange={(e) => props.onChangeCategories(e)}
          options={props.categories}
        ></SelectField>
      </div>
      <div className="w-100 border border-2 p-2 overflow-y-scroll" style={{height: "500px"}}>
        <List content={props.patterns} active={active} onClick={handleClickItem}></List>
      </div>
    </div>
  );
}

export default Aside;
