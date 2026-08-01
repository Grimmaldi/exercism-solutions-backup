defmodule HighScore do
  def new() do
    Map.new()
  end

  def add_player(scores, name, score \\ 0) do
    Map.put_new(scores, name, score)
  end

  def remove_player(scores, name) do
    Map.delete(scores, name)
  end

  def reset_score(scores, name) do
    if name not in get_players(scores) do
      add_player(scores, name)
    else
      Map.replace(scores, name, 0)
    end
  end

  def update_score(scores, name, score) do
    updated_score = fn x -> x + score end

    if name not in get_players(scores) do
      add_player(scores, name, score)
    else
      Map.update(scores, name, 0, updated_score)
    end
  end

  def get_players(scores) do
    Map.keys(scores)
  end
end
