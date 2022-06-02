import React from "react";
import { render } from "react-dom";

class SongRow extends React.Component {
    render() {
        const song = this.props.song;

        return (
            <tr>
                <td>{song.id}</td>
                <td>{song.name}</td>
                <td>{song.release_date}</td>
                <td>{song.genre_id}</td>
                <td>{song.album_id}</td>
            </tr>
        )
    }
}

class SongsTable extends React.Component {
    render() {
        const filterText = this.props.filterText;

        const rows = [];

        this.props.songs.forEach((song) => {
            if (song.name.indexOf(filterText) === -1) {
                return;
            }

            rows.push(
                <SongRow
                    song={song}/>
            );
        });

        return (
            <table>
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Release date</th>
                    <th>Genre id</th>
                    <th>Album id</th>
                </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        )
    }
}

class SearchBar extends React.Component {
    constructor(props) {
        super(props);
        this.handleFilterTextChange =
            this.handleFilterTextChange.bind(this);
    }

    handleFilterTextChange(e) {
        this.props.onFilterTextChange(e.target.value);
    }
    render() {
        return (
            <form>
                <input
                    type="text"
                    placeholder="Search..."
                    value={this.props.filterText}
                    onChange={this.handleFilterTextChange}/>
            </form>
        )
    }
}

class MainTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            filterText: ""
        };

        this.handleFilterTextChange =
            this.handleFilterTextChange.bind(this);
    }

    handleFilterTextChange(filterText) {
        this.setState({
            filterText: filterText
        });
    }

    render() {
        return (
            <div>
                <SearchBar
                    filterText={this.state.filterText}
                    onFilterTextChange={this.handleFilterTextChange} />
                <SongsTable
                    songs={this.props.songs}
                    filterText={this.state.filterText} />
            </div>
        )
    }
}

const result = fetch("http://localhost:8000/songs/")
    .then(function (response) {
        return response.json()
    });

const build = async () => {
    const rootElement = document.getElementById("root")
    render(<MainTable songs={await result}/>, rootElement)
};

build();
