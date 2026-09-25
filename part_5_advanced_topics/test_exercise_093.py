from part_4_oop.main import app


def test_todo_endpoint_has_openapi_details():
    schema = app.openapi()
    operations = [operation for path, methods in schema["paths"].items() if path.rstrip("/") == "/todos"
                  for method, operation in methods.items() if method in {"get", "post"}]
    assert operations, "请先实现 /todos 端点"
    assert all(operation.get("summary") and operation.get("description") and operation.get("tags") for operation in operations)
    schemas = schema.get("components", {}).get("schemas", {})
    assert any("example" in field or "examples" in field
               for model in schemas.values() for field in model.get("properties", {}).values()), "请为至少一个字段添加示例"
