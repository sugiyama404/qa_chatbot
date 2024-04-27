resource "aws_iam_policy_attachment" "attach" {
  name       = "iam-attach"
  roles      = ["${aws_iam_role.newworld_role.name}"]
  policy_arn = "${aws_iam_policy.newworld_policy.arn}"
}
