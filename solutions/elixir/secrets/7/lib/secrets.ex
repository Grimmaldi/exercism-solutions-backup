defmodule Secrets do
  def secret_add(secret) do
    _adder = fn(value) ->
      secret + value
    end
  end

  def secret_subtract(secret) do
    _subtractor = fn(value) ->
      value - secret
    end
  end

  def secret_multiply(secret) do
    _multiplier = fn(value) ->
      secret * value
    end
  end

  def secret_divide(secret) do
    _divider = fn(value) ->
      trunc(value / secret)
    end
  end

  def secret_and(secret) do
    _ander = fn(value) ->
      Bitwise.band(secret, value)
    end
  end

  def secret_xor(secret) do
    _xorer = fn(value) ->
      Bitwise.bxor(value, secret)
    end
  end

  def secret_combine(secret_function1, secret_function2) do
    _secret_combine = fn(value) ->
      initial_result = secret_function1.(value)
      secret_function2.(initial_result)
    end
  end
end
