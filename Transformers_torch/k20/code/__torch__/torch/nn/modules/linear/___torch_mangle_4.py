class Linear(Module):
  __parameters__ = ["weight", "bias", ]
  weight : Tensor
  bias : Tensor
  training : bool
  def forward(self: __torch__.torch.nn.modules.linear.___torch_mangle_4.Linear,
    argument_1: Tensor) -> Tensor:
    _0 = self.bias
    output = torch.matmul(argument_1, torch.t(self.weight))
    return torch.add_(output, _0, alpha=1)
