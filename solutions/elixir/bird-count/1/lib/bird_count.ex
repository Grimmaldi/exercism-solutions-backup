defmodule BirdCount do
  def today(list \\ [])

  def today(list) when list == [] do
    nil
  end

  def today(list) do
    List.first!(list)
  end

  def increment_day_count(list)

  def increment_day_count(list) when length(list) == 0 do
    [1]
  end

  def increment_day_count(list) when length(list) == 1 do
    [current_day_count] = [today(list)]
    add_count = [current_day_count + 1]
    add_count
  end

  def increment_day_count(list) when length(list) > 1 do
    incremented_value = [today(list) + 1]
    {_, rest} = Enum.split(list, 1)
    List.flatten(incremented_value, rest)
  end

  def has_day_without_birds?(list) do
    Enum.member?(list, 0)
  end

  def total(list) do
    Enum.sum(list)
  end

  def busy_days(list) do
    length(Enum.filter(list, fn x -> x >= 5 end))
  end
end
