import React, { Component } from 'react';
import './App.css';
import Person from "./Person/Person";

class App extends Component {
  state = {
    persons: [
      { id: "1", name: "Silandra", age: 18 },
      { id: "2", name: "Ajantis", age: 18 },
      { id: "3", name: "Imoen", age: 17 }
    ],
    otherState: "Some other value",
    showPersons: false
  };

  switchNameHandler = (newName) => {
    // DON'T DO THIS: this.state.persons[0].name = "Sil";
    this.setState({
      persons: [
        { name: newName, age: 18 },
        { name: "Ajantis", age: 18 },
        { name: "Imoen", age: 17 }
      ]
    });
  };

  nameChangeHandler = (event, id) => {
    const personIndex = this.state.persons.findIndex(person => {
      return person.id === id;
    });

    const person = {
      ...this.state.persons[personIndex]
    };

    person.name = event.target.value;
    
    const persons = [...this.state.persons];
    persons[personIndex] = person;

    this.setState({persons: persons});
  };

  deletePersonHandler = (index) => {
    const persons = [...this.state.persons];
    persons.splice(index, 1);
    this.setState({persons});
  };

  togglePersonsHandler = () => {
    const doesShow = this.state.showPersons;
    this.setState({showPersons: !doesShow});
  }

  render() {

    let persons = null;

    if (this.state.showPersons) {
      persons = (
      <div>
        {this.state.persons.map((person, index) => {
          return <Person
            click={() => this.deletePersonHandler(index)}
            name={person.name}
            age={person.age}
            key={person.id}
            changed={(event) => this.nameChangeHandler(event, person.id)}/>
        })}
      </div>
      );
    }

    return (
      <div className="App">
        <h1>Hi, I'm a React App!</h1>
        <p>This works!</p>
        <button onClick={this.togglePersonsHandler}>Toggle Persons</button>
        {persons}
      </div>
    );
    // return React.createElement("div", {className: "App"}, React.createElement("h1", null, "Does this work yet?"));
  }
}

export default App;
