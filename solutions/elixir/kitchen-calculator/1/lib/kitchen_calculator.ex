defmodule KitchenCalculator do
  def get_volume(volume_pair) do
    { _, volume } = volume_pair
    volume
  end

  def to_milliliter(volume_pair = { :cup, _ }) do
    { _, volume } = volume_pair
    { :milliliter, volume * 240.0 }
  end

  def to_milliliter(volume_pair = { :fluid_ounce, _ }) do
    { _, volume } = volume_pair
    { :milliliter, volume * 30.0 }
  end

  def to_milliliter(volume_pair = { :teaspoon, _ }) do
    { _, volume } = volume_pair
    { :milliliter, volume * 5.0 }
  end

  def to_milliliter(volume_pair = { :tablespoon, _ }) do
    { _, volume } = volume_pair
    { :milliliter, volume * 15.0 }
  end

  def to_milliliter(volume_pair = { :milliliter, _ }) do
    { _, volume } = volume_pair
    volume_float = volume / 1
    { :milliliter, volume_float }
  end

  def from_milliliter(volume_pair, unit) do
    value_pair_in_milliliters = (to_milliliter(volume_pair))
    {_, milliliter_amount } = value_pair_in_milliliters
    number_of_units_in_ml = units_of_measure_in_ml(unit)
    total_of_selected_unit = milliliter_amount / number_of_units_in_ml
    {unit, total_of_selected_unit}
  end

  defp units_of_measure_in_ml (measure) do
      cond do
        measure == :milliliter -> 1.0
        measure == :teaspoon -> 5.0
        measure == :tablespoon -> 15.0
        measure == :fluid_ounce -> 30.0
        measure == :cup -> 240.0
        end
    end

  def convert(volume_pair, unit) do
    milliliter_volume_pair = to_milliliter(volume_pair)
    from_milliliter(milliliter_volume_pair, unit)
  end
end
