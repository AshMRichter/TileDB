/**
 * @file   tdbpp_sparse_write_unordered_1_again.cc
 *
 * @section LICENSE
 *
 * The MIT License
 *
 * @copyright Copyright (c) 2017 TileDB, Inc.
 * @copyright Copyright (c) 2016 MIT and Intel Corporation
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * @section DESCRIPTION
 *
 * It shows how to write unordered cells to a sparse array in a single write.
 * This time we write 4 cells.
 *
 * You need to run the following to make this work:
 *
 * ./tiledb_sparse_create
 * ./tiledb_sparse_write_unordered_1_again
 */

#include <tdbpp>

int main() {
  tdb::Context ctx;
  tdb::Array array = ctx.array_get("my_sparse_array");
  tdb::Query query = array.write();

  query.buffer_list({"a1", "a2", "a3", TILEDB_COORDS});

  // clang-format off
  std::vector<int> a1_buff = {107, 104, 106, 105};
  auto a2_buff = tdb::make_var_buffers<std::string>({"yyy", "u", "w", "vvvv"});
  std::vector<float> a3_buff = {107.1, 107.2, 104.1, 104.2, 106.1, 106.2, 105.1, 105.2};
  std::vector<uint64_t> coords_buff = {3, 4, 3, 2, 3, 3, 4, 1};

  query.set_buffer<tdb::type::INT32>("a1", a1_buff);
  query.set_buffer<tdb::type::CHAR>("a2", a2_buff);
  query.set_buffer<tdb::type::FLOAT32>("a3", a3_buff);
  query.set_buffer<tdb::type::UINT64>(TILEDB_COORDS, coords_buff);
  query.layout(TILEDB_UNORDERED);

  query.submit();

  return 0;
}
