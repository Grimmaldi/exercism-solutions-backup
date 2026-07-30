defmodule HighSchoolSweetheart do
  def first_letter(name) do
    name |> String.trim() |> String.first()
  end

  def initial(name) do
    name |> first_letter() |> String.upcase() |> Kernel.<>(".")
  end

  def initials(full_name) do
    [first, last] = String.split(full_name, " ")
    first_init = initial(first)
    last_init = initial(last)
    "#{first_init} #{last_init}"
  end

  def pair(full_name1, full_name2) do
    n1 = initials(full_name1)
    n2 = initials(full_name2)

    """
    ❤-------------------❤
    |  #{n1}  +  #{n2}  |
    ❤-------------------❤
    """
  end
end
