defmodule GuessingGame do
  def compare(secret_number, guess \\ :no_guess) do
    cond do
      guess == :no_guess -> "Make a guess"
      secret_number == guess -> "Correct"
      ((guess + 1) == secret_number) or ((guess - 1) == secret_number) -> "So close"
      (guess > secret_number) -> "Too high"
      (guess < secret_number) -> "Too low"
    end
  end
end
