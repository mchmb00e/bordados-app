import { useEffect, useState } from "react";
import Aside from "./components/Aside"; // Ensure this component is correctly imported

export default function App() {
  const [categories, setCategories] = useState([]);
  const [patterns, setPatterns] = useState([]);
  const [textAux, setTextAux] = useState("");  // Track text input state

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/categories/");
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log("Categorías obtenidas:", data);
        setCategories(data);
      } catch (error) {
        console.error("Error al obtener categorías:", error);
      }
    };

    fetchCategories();
  }, []);

  const fetchPatternsByCategory = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/patterns/?category=${id}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setPatterns(data);
    } catch (error) {
      console.error(`Error al obtener patrones para la categoría ${id}:`, error);
    }
  };

  const fetchPatternsByFavorite = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/patterns/?favorite=true`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setPatterns(data);
    } catch (error) {
      console.error(`Error al obtener patrones favoritos:`, error);
    }
  };

  const fetchPatternsBySubstring = async (substr) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/patterns/?substring=${substr}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setPatterns(data);
    } catch (error) {
      console.error(`Error al obtener patrones para el substring ${substr}:`, error);
    }
  };

  const handleCategorySelection = (id) => {
    fetchPatternsByCategory(id);
  };

  const handlePatternClick = (id) => {
    console.log(id);  // Handle the pattern click (add more logic as needed)
  };

  const handleClickFavorites = () => {
    fetchPatternsByFavorite();
  };

  const handleChangeText = (text) => {
    setTextAux(text);  // Update the state with the input text
  };

  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key === "Enter") {
        console.log("Buscar por substring:", textAux);
        fetchPatternsBySubstring(textAux);
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    return () => {
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, [textAux]);  // Dependency on textAux so that it updates properly

  return (
    <Aside
      className="col-3 p-2"
      categories={categories}
      patterns={patterns}
      onChangeCategories={handleCategorySelection}
      onClickPattern={handlePatternClick}
      onClickFavorites={handleClickFavorites}
      onChangeText={handleChangeText}
    />
  );
}
