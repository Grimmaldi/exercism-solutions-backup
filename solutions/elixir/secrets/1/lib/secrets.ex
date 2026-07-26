defmodule Secrets do
  def secret_add(secret) do
    adder = fn(value) ->
      secret + value
    end
  end

  def secret_subtract(secret) do
    # Please implement the secret_subtract/1 function
    subtractor = fn(value) ->
      value - secret
    end
  end

  def secret_multiply(secret) do
    multiplier = fn(value) ->
      secret * value
    end
  end

  def secret_divide(secret) do
    divider = fn(value) ->
      trunc(value / secret)
    end
  end

  def secret_and(secret) do
    ander = fn(value) ->
      Bitwise.band(secret, value)
    end
  end

  def secret_xor(secret) do
    xorer = fn(value) ->
      Bitwise.bxor(value, secret)
    end
  end

  def secret_combine(secret_function1, secret_function2) do
    secret_combine = fn(value) ->
      initial_result = secret_function1.(value)
      combined_result = secret_function2.(initial_result)
      combined_result
    end
  end
end
